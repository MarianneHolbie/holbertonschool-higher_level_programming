"""
    initialize package Base class with class and static method
    2 subclass : Rectangle and Square
    
    Package Base class
       ATTRIBUTS
        ==================
            __nb_objects : private, count

            id : id of each form

        METHOD
        ==================

            __init__ : constructor fo Base class

            @classMethod:

                save_to_file : write json string in list_dictionary

                create: create instance of subclasse and update
                        value with **dict

                load_from_file: load file of instance subclass, extract
                                form and create

            @StaticMethod:

                to_json_string : static method to return json string
                                 representation

                from_json_string : return list of the JSON string
                                   representation json_string
"""