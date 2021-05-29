import numpy as np 

def function(x):

	c3 = x
	v3 = x
	x = 9
	paths = []
	try:
		if c3 > 6:
			v3 = v3+x
			v3 = v3/x
			paths.append(1)
		else:
			x = 6/c3
			v3 = v3+v3
			paths.append(2)
		if c3 <= 1:
			v3 = v3*v3
			v3 = 5/v3
			v3 = c3+1
			paths.append(3)
		else:
			x = x/8
			v3 = c3+3
			c3 = 4/7
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		v3 = c3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))