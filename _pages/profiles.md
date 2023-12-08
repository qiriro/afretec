---
layout: about
permalink: /people/
title: members
description: List of members
nav: true
nav_order: 2
---
{% for member in site.data.members %}
  <div class="card hoverable">
    <div class="row no-gutters">
      <div class="col-sm-4 col-md-3">
         <img class="card-img-top" src="{{site.url}}{{site.baseurl}}/assets/img/members/resized/{{member['PhotoUrl']}}">
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
{% endfor %}

