import bpy
import random

def colorize(obj):
    if not obj.type in ['MESH']:
        return
    
    mesh = obj.data    
        
    if not mesh.vertex_colors:
        mesh.vertex_colors.new("ID_MAP")
    else:
        print(obj.name + " already has a ID_MAP")
        return
    
    color_layer = mesh.vertex_colors["ID_MAP"]
    pal = bpy.data.palettes["ID_MAP_Palette"]    
    obj_color = [random.random() for i in range(3)]
    
    i = 0
    for poly in mesh.polygons:
        for idx in poly.loop_indices:
            color_layer.data[i].color = obj_color
            i+=1
    
    pal_color = pal.colors.new()
    pal_color.color = obj_color

def main(context):    
    if bpy.data.palettes["ID_MAP_Palette"] is None:
        bpy.data.data.palettes.new("ID_MAP_Palette")
    
    for ob in bpy.context.selected_objects:
        colorize(ob)


class ColorIdMapOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.vertex_color_id_map"
    bl_label = "Vertex Color Id Map"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ColorIdMapOperator)


def unregister():
    bpy.utils.unregister_class(ColorIdMapOperator)


if __name__ == "__main__":
    register()
    print('register')
    # test call
    #bpy.ops.object.simple_operator()
