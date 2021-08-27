def run():
    pass
    my_list = [1,"Hello", True, 4.5]
    my_dict = { "First_name:", "Ulises", "Last_name:", "Ramirez"}

    super_list=[
        { "First_name:", "Ulises", "Last_name:", "Ramirez"},
        { "First_name:", "Randal", "Last_name:", "Lopez"},
        { "First_name:", "Alan", "Last_name:", "Moreno"},
        { "First_name:", "Daniela", "Last_name:", "Ordonez"},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5,6,7,8,9,10,11,12],
        "integer_nums":[-1,-2,0,1,2,3,4,5,6,7,],
        "floating_point_nums":[1.2,1.3,1.4,1.5,1.6]
    }

    for key, value in super_dict.items():
        print(key, "-",  value) 


if __name__ == '__main__':
    run()
