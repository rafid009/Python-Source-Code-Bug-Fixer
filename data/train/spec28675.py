import numpy as np 

def function(x):

	j1 = 1
	u3 = 5
	paths = []
	try:
		if j1 < 3:
			u3 = 2*6
			paths.append(1)
		else:
			u3 = j1*j1
			paths.append(2)
		if x <= 9:
			u3 = x/9
			paths.append(3)
		else:
			u3 = u3*1
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))