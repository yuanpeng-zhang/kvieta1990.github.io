---
layout: page
category: pages
navigation_weight: 2
---

To start a Jekyll instance
==========================

1. Clone the desired `pages.ornl.gov` repository
2. `cd` into the folder
3. Run `gem install jekyll bundler`
4. Run `bundle update --bundler`
5. To start a web server locally, run `bundle exec jekyll serve --incremental`

Note:
-----
Sometimes the pages are not refreshed correctly. Stop the web server, completely delete the `_site` folder, then restart the server

Create sphinx pages
===================

1. Run `sphinx-quickstart`. Some of the options I've selected:
 - `Separate source and build directories` `y` (otherwise make clean deletes useful stuff)
 - `Name prefix for templates and static dir [_]:`
 - `Name of your master document (without suffix) [index]:` `documentation_index`
 - `githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:` `y` (make sure it plays nicely with jekyll)
2. I've modified the `Makefile` so that the build directory will be called `sphinx`: 
~~~~~ make
BUILDDIR      = sphinx 
~~~~~
3. run `make html`
4. Add the following lines to `_config.yml`, to copy the correct folders:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
include: 
       - _static
       - _images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5. Add the CSS file with ORNL standard look to `source/_static`. I've used CSS snippets from [ORNL's standards webpage](https://standards.ornl.gov/). See UI Components.
6. Add the layout file to `source/_templates`
   {% highlight html linenos %}
   <!-- This overrides alabaster theme with ORNL one from https://standards.ornl.gov/ -->
   {% raw %}
   {% extends "basic/layout.html" %}
   {% block linktags %}
   <link rel='stylesheet' id='custom-css'  href='_static/custom.css' type='text/css' media='all' />
   {% endblock %}
   
   {% block extrahead %}
   <header class="site-header" role="banner">
     <nav class="navbar navbar-default " role="navigation">
       <div class="container">
         <div class="row">
           <div class="site-navigation-inner col-sm-12">
             <div class="navbar-header">
               <div class="logo">
                  <a href="http://www.ornl.gov">
                    <img src="http://STANDARDS.ORNL.GOV/wp-content/uploads/2017/09/ORNL-white.png" alt="ORNL Logo">
                  </a>
               </div>
             </div>
             <div class="site-title nav navbar-nav">
               <a href="index.html">
                 Direct Geometry Spectroscopy
               </a>
             </div>
           </div>
         </div>
       </div>
     </nav>
   
     <div class="secondary">
       <nav class="navbar  secondary-nav" role="navigation">
         <div class="container">
           <div class="row">
             <div class="site-navigation-inner col-sm-12">
               <div>
                 <ul id="menu-main-menu" class="nav navbar-nav">
                   <li id="menu-item-1" class="menu-item"><a href="/sphinx/html/documentation_index.html">Documentation</a></li>
                   <li id="menu-item-3" class="menu-item"><a href="/contact.html">Contact Us</a></li>
                 </ul>
               </div>
             </div>
           </div>
         </div>
       </nav>
     </div>
   </header>{% endblock %}
   
   {% block relbar1 %}{% endblock %}
   {% block relbar2 %}{% endblock %}
   
   {% block footer %}
   <div class="branding-sponsor">
     <p>Oak Ridge National Laboratory is managed by UT-Battelle LLC for the US Department of Energy</p>
   </div>
   <div id="footer-area">
     <footer class="site-footer" role="contentinfo">
       <div class="site-info container">
         <div class="row">
           <div class="col-md-3">
             <a href="https://ut-battelle.org"><img class="img-responsive" src="http://STANDARDS.ORNL.GOV/wp-content/uploads/2017/10/ut-battelle.png"></a>
           </div>
           <div class="col-md-6 mandatory-links">
             <a href="https://www.ornl.gov/ornl/contact-us/Security--Privacy-Notice">Privacy</a> | <a href="https://www.ornl.gov/content/accessibility">Accessibility/508</a> | <a href="https://www.ornl.gov/content/notice-nondiscrimination-and-accessibility-requirements">Nondiscrimination/1557</a>
           </div>
           <div class="col-md-3">
             <a href="https://www.energy.gov/science/office-science"><img class="img-responsive" src="http://STANDARDS.ORNL.GOV/wp-content/uploads/2017/10/doe-science.png"></a>
           </div>
         </div>
       </div>
     </footer>
   </div>
   {% endblock %}
   {% endraw %}
   {% endhighlight %}
{:start="7"}
7. Modify jekyll's CSS
