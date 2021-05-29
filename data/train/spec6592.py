import numpy as np 

def function(x):

	o2 = x
	u6 = x
	paths = []
	try:
		if o2 <= 3:
			o2 = 3-o2
			x = x/9
			u6 = 6*u6
			paths.append(1)
		else:
			o2 = 7/3
			o2 = 7-0
			o2 = x+5
			paths.append(2)
		if u6 <= 4:
			x = x/1
			o2 = 1*u6
			x = 4-7
			paths.append(3)
		else:
			u6 = 5-o2
			x = x/o2
			o2 = x+o2
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))