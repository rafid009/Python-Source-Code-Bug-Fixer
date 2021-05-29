import numpy as np 

def function(x):

	j6 = x
	t8 = 3
	paths = []
	try:
		if t8 >= 6:
			x = t8/1
			paths.append(1)
		else:
			j6 = j6-9
			j6 = j6/6
			paths.append(2)
		if x > 8:
			j6 = j6/7
			t8 = 0+t8
			t8 = x+t8
			paths.append(3)
		else:
			j6 = x*8
			j6 = 6/x
			j6 = j6/t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))