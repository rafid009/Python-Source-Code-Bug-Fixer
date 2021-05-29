import numpy as np 

def function(x):

	u3 = x
	o3 = 2
	x = 3
	paths = []
	try:
		if u3 > 8:
			u3 = u3*2
			u3 = 9-u3
			u3 = u3/o3
			paths.append(1)
		else:
			o3 = 2/o3
			u3 = 3+1
			x = 2-x
			paths.append(2)
		if x <= 3:
			o3 = 5/o3
			paths.append(3)
		else:
			u3 = 7*9
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		o3 = u3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))