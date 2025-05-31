def paint_calc(height,width,coverage):
    cover = 5
    area=int(height*width)
    num_cans=round(area/cover)
    print(f"the number of cans needed are {num_cans} cans")
t_height=int(input("What is the height:"))
t_width=int(input("What is the width:"))
cover=5
paint_calc(height=t_height,width=t_width,coverage=cover)
