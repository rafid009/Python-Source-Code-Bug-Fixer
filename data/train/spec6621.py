import numpy as np 

def function(x):

	v1 = x
	u3 = x
	paths = []
	try:
		if x < 9:
			x = 6*x
			x = 0+x
			u3 = v1+1
			paths.append(1)
		else:
			u3 = v1/2
			u3 = u3/x
			v1 = v1/6
			paths.append(2)
		if u3 < 7:
			x = x/x
			paths.append(3)
		else:
			u3 = u3+8
			u3 = 1*v1
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