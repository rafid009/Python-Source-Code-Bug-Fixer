import numpy as np 

def function(x):

	y6 = x
	i3 = 3
	paths = []
	try:
		if y6 > 3:
			y6 = 6*y6
			x = x/2
			i3 = 2-x
			paths.append(1)
		else:
			x = x*0
			i3 = i3/i3
			y6 = y6-3
			paths.append(2)
		if i3 >= 2:
			y6 = 3-5
			x = i3+x
			x = x*9
			paths.append(3)
		else:
			x = x+y6
			y6 = y6-6
			x = i3-9
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		y6 = i3**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))