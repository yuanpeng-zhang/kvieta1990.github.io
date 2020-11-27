import sys
from DGSPlanner import DGSPlannerGUI
from mantidqt.gui_helper import get_qapplication
import qtpy
import mantid
import numpy


def generate_picture(filename, **options):
    app, within_mantid = get_qapplication()
    planner = DGSPlannerGUI.DGSPlannerGUI()
    planner.show()

    if options:
        try:
            # instrument related
            instrument = options.get('Instrument')
            if instrument:
                index = planner.instrumentWidget.instrumentList.index(instrument)
                planner.instrumentWidget.combo.setCurrentIndex(index)
                planner.instrumentWidget.instrumentSelected(instrument)
            Ei = options.get('Ei', 10)
            planner.instrumentWidget.editEi.setText(str(Ei))
            planner.instrumentWidget.editEi.textEdited.emit(str(Ei))
            S2 = options.get('S2', 0)
            planner.instrumentWidget.editS2.setText(str(S2))
            planner.instrumentWidget.editS2.textEdited.emit(str(S2))
            psimin = float(options.get('psi_min', 0))
            psimax = float(options.get('psi_max', 0))
            psistep = float(options.get('psi_step', 1))
            #if len(numpy.arange(psimin, psimax + 0.1 * psistep, psistep)) > 10:
            #    raise ValueError("This will open a MessageBox, so it will hang if you can't reply yes")
            index = planner.instrumentWidget.goniomodel.index(0,3)
            planner.instrumentWidget.goniomodel.setData(index,psimin)
            index = planner.instrumentWidget.goniomodel.index(0,4)
            planner.instrumentWidget.goniomodel.setData(index,psimax)
            index = planner.instrumentWidget.goniomodel.index(0,5)
            planner.instrumentWidget.goniomodel.setData(index,psistep)
            
            # UB related
            a = options.get('a', 1)
            b = options.get('b', 1)
            c = options.get('c', 1)
            alpha = options.get('alpha', 90)
            beta = options.get('beta', 90)
            gamma = options.get('gamma', 90)
            u = options.get('u', '0, 0, 1')
            v = options.get('v', '1, 0, 0')
            __tempws = mantid.simpleapi.CreateSingleValuedWorkspace()
            mantid.simpleapi.SetUB(__tempws, a, b, c, alpha, beta, gamma, u, v)
            ol = __tempws.sample().getOrientedLattice()
            planner.classic.updateOL(ol)
            planner.classic.latt_ux, planner.classic.latt_uy, planner.classic.latt_uz = [float(x) for x in u.split(',')]
            planner.classic.latt_vx, planner.classic.latt_vy, planner.classic.latt_vz = [float(x) for x in v.split(',')]
            planner.classic.updateGui()
            planner.updateUB(ol)
            planner.matrix.UBmodel.updateOL(ol)
            
            # plot options
            planner.dimensionWidget._editBasis1.setText(options.get('proj_u','1,0,0'))
            planner.dimensionWidget._editBasis2.setText(options.get('proj_v','0,1,0'))
            planner.dimensionWidget._editBasis3.setText(options.get('proj_w','0,0,1'))
            planner.dimensionWidget.validateBasis()
            planner.dimensionWidget.dimMin[0] = options.get('proj_u_min', -numpy.inf)
            planner.dimensionWidget.dimMax[0] = options.get('proj_u_max', numpy.inf)
            planner.dimensionWidget.dimStep[0] = options.get('proj_u_step', 0.05)
            planner.dimensionWidget.dimMin[1] = options.get('proj_v_min', -numpy.inf)
            planner.dimensionWidget.dimMax[1] = options.get('proj_v_max', numpy.inf)
            planner.dimensionWidget.dimStep[1] = options.get('proj_v_step', 0.05)
            planner.dimensionWidget.dimMin[2] = options.get('proj_w_min', -numpy.inf)
            planner.dimensionWidget.dimMax[2] = options.get('proj_w_max', numpy.inf)
            planner.dimensionWidget.dimStep[2] = options.get('proj_w_step', 0.05)
            planner.dimensionWidget.dimMin[3] = options.get('e_min', -numpy.inf)
            planner.dimensionWidget.dimMax[3] = options.get('e_max', numpy.inf)
            planner.dimensionWidget.dimStep[3] = options.get('e_step', 1)
            dimension_order = options.get('dimension_order', [0, 1, 2, 3])
            if set(dimension_order)!=set([0, 1, 2, 3]):
                raise ValueError('Dimension order is invalid')
            original = [0, 1, 2, 3]
            swap = []
            for i in range(4):
                other=original.index(dimension_order[i])
                original[i], original[other]=original[other], original[i]
                swap.append(other)

            planner.dimensionWidget._comboDim1.currentIndexChanged.emit(swap[0])
            planner.dimensionWidget._comboDim2.currentIndexChanged.emit(swap[1])
            planner.dimensionWidget._comboDim3.currentIndexChanged.emit(swap[2])
            planner.dimensionWidget._comboDim4.currentIndexChanged.emit(swap[3])
        except Exception as err:
            mantid.logger.error(str(err))
            raise(err)
        try:
            planner.updateFigure()
        except Exception as err:
            mantid.logger.error("Parameters: " + str(planner.masterDict))
            raise(err)
    pix = qtpy.QtGui.QPixmap(planner.size())
    planner.render(pix)
    # some canvases are not rendered correctly the first time (black boxes)
    planner.render(pix)

    a=pix.save(filename)

    planner.close()
    app.quit()

if __name__=='__main__':
    #app, within_mantid = get_qapplication()
    generate_picture('~/Desktop/dgs-fig.png',
                     a=2, 
                     b=2, 
                     u='1,0,0', 
                     v='0,1,0',
                     Instrument='HYSPEC', 
                     Ei=30, 
                     S2=30, 
                     psi_min=0, 
                     psi_max=90, 
                     psi_step=15,
                     dimension_order=[0,1,2,3], 
                     proj_u='1,1,0',
                     proj_u_min=-3,
                     proj_u_max=3,
                     proj_u_step=0.1,
                     e_min=-1, 
                     e_max=1)    
    sys.exit()
