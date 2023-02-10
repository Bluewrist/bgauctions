{% extends 'base.html' %} 
 {% load static %}


 <nav aria-label="Page navigation example mt-3">
  <ul class="pagination mt-5">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
  {% block content %}
<div class="container">
  <div class="row mt-23 ">
    <div class="col Left-navigation">
      <div class="card">
        <div class="card-body">
          <div class="card-title">Categories</div>
          <div class="card mt-2">
            <div class="card-body">
              <div class="card-title"><a href="{% url 'home'%}">All</a></div>
              <ul>
                {% for topic in category %}
                <li><a href="{% url 'home' %}?q={{ topic.name }}" >{{topic.name }}</a></li>
                
                {% endfor %}
              </ul>
            </div>
          </div>
        </div>
      </div>
      
    </div>
    <div class="col-6">
      <header class="justyfy-content center" >On Auction</header>
      <header class="justyfy-content center" >({{ product_count  }})  Products Availlable on Auction</header>

      
      {% for p in bid  %} 
      <div class="card shadow-0 border rounded-3 mt-5 mb-5">
        <div class="card-body">
          <div class="row">
            <div class="col-md-12 col-lg-3 col-xl-3 mb-4 mb-lg-0">
              <div class="bg-image hover-zoom ripple rounded ripple-surface">
                <img src="{{ p.product_thumbnail.url }}"
                  class="w-100" />
                <a href="#!">
                  <div class="hover-overlay">
                    <div class="mask" style="background-color: rgba(253, 253, 253, 0.15);"></div>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-md-6 col-lg-6 col-xl-6">
              <h5>{{ p.product_name }}</h5>
              
              <p class=" mb-4 mb-md-0">
                {{ p.product_description }}
              </p>
            </div>
            <div class="col-md-6 col-lg-3 col-xl-3 border-sm-start-none border-start">
              <h6 class="text-success">Starting Price</h6>
              <div class="d-flex flex-row align-items-center mb-1">
                <h4 class="mb-1 me-1 text-danger">USD {{p.bid_start_price|floatformat:2 }}</h4>
                
              </div>
              
              <div class="d-flex flex-column mt-4">
               <a href="{% url 'product' p.id %}">
                   <button class="btn btn-primary btn-sm" type="button" >
                   Details
               </button>
               </a>
               {% if user.is_authenticated %}
               <a href="{% url "make_bid" p.pk %}">
                <button class="btn btn-outline-primary btn-sm mt-2" type="button">
                  Bid Now
                </button>
               </a>
               {% else %}
               {% endif %}
              </div>
            </div>
            
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
    <div class="col sidebar">
      <div class="card">
        <div class="card-body">
          <div class="card-title">Bidders</div>
          {%  for b in username %}
          <div class="card mt-2">
            <div class="card-body">
              <div class="card-title">@{{ b.username }}</div>
            </div>
          </div>
          {%  endfor %}
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}


<div class="more-views">
                                <div class="slider-items-products">
                                  <div id="gallery_02" class="product-flexslider hidden-buttons product-img-thumb">
                                    <div class="slider-items slider-width-col4 block-content">
                                      {% for pi in product.product_img_set.all %}
                                     <div class="more-views-items p-3"class="col-md-4" > 
                                      <img class="thumbnail" id="product-zoom0"  src="{{ pi.images.url }}" class="img-fluid" style="height: 100px; object-fit: contain;" alt="product-image"/> 
                                      </a>
                                      </div>
                                      {% endfor %}
                                    </div>
                                  </div>
                                </div>
                              </div>