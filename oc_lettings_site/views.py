from django.shortcuts import render


"""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
non finibus neque cursus id."""


def index(request):
    """function to return the index.html page"""
    return render(request, "index.html")


def trigger_error(request):
    """function to trigger the html page 500 Error"""
    division_by_zero = 1 / 0  # noqa: F841
