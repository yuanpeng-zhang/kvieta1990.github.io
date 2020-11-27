---
layout: page
title: Gitlab Pages Demo
category: pages
navigation_weight: 1
---

**Summary**: This page is an example of what a site might look like if it was created using the ORNL Pages automated static site service. This service leverages Git, Docker, Gitlab CI Runners, and Jekyll to allow users to maintain their own sites in Markdown or HTML through ORNL's internal GitLab services and publish those sites internally or externally. Additionally, users can choose between no authenication, XCAMS, UCAMS, or UCAMS + RSA for their sites.

Let's test some code:

{% highlight html linenos %}

<!-- News card -->
<div class="research-card-wrapper">
    <div class="news-card">
        <h3>News</h3>
        <p>Teaser goes here.
        </p>
        <a href="" class="button">Read</a>
    </div>
</div>

{% endhighlight %}

{% highlight css linenos %}
footer {
    background-color: #006699;
}
{% endhighlight %}


**Links**:
* [GitLab: How to Create a Project](https://docs.gitlab.com/ee/gitlab-basics/create-project.html)
* [What is Docker?](https://www.docker.com/what-docker)
* [Kramdown Syntax](https://kramdown.gettalong.org/syntax.html)
* [How to Use Jekyll](https://jekyllrb.com/docs/home/)

