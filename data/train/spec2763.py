import numpy as np 

def function(x):

	u3 = x
	o8 = 0
	paths = []
	try:
		if u3 <= 8:
			o8 = o8+u3
			x = 7+u3
			paths.append(1)
		else:
			o8 = 7+o8
			u3 = u3+0
			o8 = o8*3
			paths.append(2)
		if x <= 5:
			o8 = o8*u3
			u3 = u3+7
			paths.append(3)
		else:
			x = x/7
			u3 = 6+0
			x = x*x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		o8 = u3**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))