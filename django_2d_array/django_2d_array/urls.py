from django.urls import path
import app.views




urlpatterns = [
    path('grid/init/',                       app.views.grid_init ),
    path('grid/grid_generator/<int:columns>/<int:rows>/',             app.views.grid_generator, name = "grid_generator" ),
    path('grid/rotate/<int:rotations>/',     app.views.grid_rotate ),
    path('',                                 app.views.index, name = 'index' ),
]

