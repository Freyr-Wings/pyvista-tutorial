"""
.. _ref_lighting_properties_example:

Lighting Properties
~~~~~~~~~~~~~~~~~~~

Control aspects of the rendered mesh's lighting such as Ambient, Diffuse,
and Specular. These options only work if the ``lighting`` argument to
``add_mesh`` is ``True`` (it's ``True`` by default).

You can turn off all lighting for the given mesh by passing ``lighting=False``
to ``add_mesh``.

See the ``add_mesh`` docs for lighting options:
https://docs.pyvista.org/api/plotting/_autosummary/pyvista.Plotter.add_mesh.html
"""
# sphinx_gallery_thumbnail_number = 4
import pyvista as pv
from pyvista import examples

mesh = examples.download_st_helens().warp_by_scalar()

cpos = [(575848.0, 5128459.0, 22289.0), (562835.0, 5114981.5, 2294.5), (-0.5, -0.5, 0.7)]

###############################################################################
# First, lets take a look at the mesh with default lighting conditions
mesh.plot(cpos=cpos, show_scalar_bar=False)

###############################################################################
# What about with no lighting?
mesh.plot(lighting=False, cpos=cpos, show_scalar_bar=False)

###############################################################################
# Demonstration of the specular property
#
# Feel free to adjust the specular value in the ``s`` variable.
p = pv.Plotter(shape=(1, 2), window_size=[1500, 500])

p.subplot(0, 0)
p.add_mesh(mesh, show_scalar_bar=False)
p.add_text('No Specular')

p.subplot(0, 1)
specular = 1.0
p.add_mesh(mesh, specular=specular, show_scalar_bar=False)
p.add_text(f'Specular of {specular}')

p.link_views()
p.view_isometric()
p.show(cpos=cpos)

###############################################################################
# Specular power (feel free to adjust)
mesh.plot(specular=0.5, specular_power=15, cpos=cpos, show_scalar_bar=False)

###############################################################################
# Demonstration of all diffuse, specular, and ambient in use together
# (feel free to adjust)
mesh.plot(diffuse=0.5, specular=0.5, ambient=0.5, cpos=cpos, show_scalar_bar=False)

###############################################################################
# For detailed control over lighting conditions in general see the
# `lighting examples <https://docs.pyvista.org/examples/index.html#lighting>`_
