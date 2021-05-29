import numpy as np 

def function(x):

	u5 = 6
	v9 = 3
	paths = []
	try:
		if u5 >= 7:
			x = x+6
			u5 = u5-u5
			v9 = 9-v9
			paths.append(1)
		else:
			x = 5*3
			paths.append(2)
		if u5 < 6:
			x = 5*4
			v9 = x-v9
			paths.append(3)
		else:
			v9 = v9-x
			x = u5-8
			x = u5-0
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))