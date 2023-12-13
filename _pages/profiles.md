---
layout: page
permalink: /people/
title: cluster members
description: 
nav: true
nav_order: 2
---
  <article>
          <div class="profile float-right">
            <a href="https://qiriro.com">
              <img
                class="img-fluid z-depth-1 rounded"
                src="{{site.url}}{{site.baseurl}}/assets/img/members/resized/Kizito_Nkurikiyeyezu.jpg"
                alt="Kizito NKURIKIYEYEZU"
              />
            </a>
             <br>
             <br>
            <div class="address">
              <p class="post">
                  <a href="mailto:kizito@duck.com" class="card-link"><i class="fas fa-envelope"></i></a>
<a href="https://rw.linkedin.com/in/qiriro" class="card-link" target="_blank"><i class="fab fa-linkedin"></i></a>
<a href="https://orcid.org/0000-0002-9128-7080" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
<a href="https://twitter.com/qiriro_" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>

<!-- Add Google Scholar link -->

<a href="https://scholar.google.com/citations?user=88SFvqYAAAAJ&hl=en" class="card-link" target="_blank"><i class="ai ai-google-scholar"></i></a>

<!-- Add ResearchGate link -->

<a href="https://www.researchgate.net/profile/Kizito-Nkurikiyeyezu" class="card-link" target="_blank"><i class="ai ai-researchgate"></i></a>

<!-- Add Personal Website link -->

<a href="https://qiriro.com/" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
              </p>
            </div>
          </div>
          <div class="clearfix">
            <p>

<a href="https://qiriro.com">Kizito Nkurikiyeyezu </a> is the lead for the AFRETEC Health Cluster and an academician at the University of Rwanda. He has also served as a Visiting Scholar at Queen’s University Belfast in the UK and as an Invited Researcher at Aoyama Gakuin University in Japan. Additionally, he held a brief position as an Invited Scholar at Université de Saint-Etienne in France.

</p>
<p>
  His research aims to develop indigenous solutions to healthcare challenges in Rwanda and Africa, with a specific focus on the application of artificial intelligence (AI). During his Ph.D. research, he developed a novel intelligent thermal comfort provision system that estimates individuals' thermal comfort levels based on variations in their heart rate, reflecting their bodies' response to the surrounding environment.
</p>
<p>
  He earned his Ph.D. from Aoyama Gakuin University in Tokyo, Japan. He holds an MS in Electrical & Computer Engineering from Oklahoma Christian University, USA, and a BS in Electrical Engineering from the same institution.
</p>
          </div>
        </article>
{% for member in site.data.members %}
  <div class="card hoverable">
    <div class="row no-gutters">
      <div class="col-sm-4 col-md-3">
         <img class="card-img-top" src="{{site.url}}{{site.baseurl}}/assets/img/members/resized/{{member['Image']}}">
      </div>
      <div class="team col-sm-8 col-md-9">
        <div class="card-body">
          <a href="{{ member['Website']}}">
            <h5 class="card-title">{{ member['Title'] }} {{ member['FirstName'] }} {{ member['LastName'] }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ member['Occupation'] }}</h6>
            <p class="card-text">{{ member['Expertise'] }}</p>
          </a>
          <a href="mailto:{{ member['Email'] }}" class="card-link"><i class="fas fa-envelope"></i></a>
          {% if member['LinkedIn'] %}
            <a href="{{ member['LinkedIn'] }}" class="card-link" target="_blank"><i class="fab fa-linkedin"></i></a>
          {% endif %}

          {% if member['ORCID'] %}
            <a href="{{ member['ORCID'] }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
          {% endif %}
          {% if member['Twitter'] %}
            <a href="{{ member['Twitter'] }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
          {% endif %}
          <p class="card-text">
            <small class="test-muted"><i class="fas fa-thumbtack"></i> {{ member['Institution'] }}, {{ member['Country'] }}</small>
          </p>
        </div>
      </div>
    </div>
  </div>
  <br>
{% endfor %}
