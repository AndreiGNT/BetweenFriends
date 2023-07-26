<header class="site-header" >
            <nav class="navbar navbar-expand-lg bg-body-tertiary ">
                <div class="container">
                    <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarToggle">
                        <div class="navbar-nav mr-auto">
                            <a class="nav-link active" aria-current="page"href="{% url 'blog-home' %}">Home</a>
                            <a class="nav-link" href="{% url 'blog-about' %}">About</a>
                        </div>
                    </div>
                    <!-- Navbar Right Side -->
                    <div class="navbar-nav">
                        <a class="nav-item nav-link" href="#">Login</a>
                        <a class="nav-item nav-link" href="#">Register</a>
                    </div>
                </div>
            </nav>
</header>