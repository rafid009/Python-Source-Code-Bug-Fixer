import numpy as np 

def function(x):

	u3 = 4
	i4 = x
	paths = []
	try:
		if i4 > 6:
			x = u3*x
			u3 = u3-i4
			u3 = u3/9
			paths.append(1)
		else:
			i4 = 8+i4
			u3 = u3/6
			paths.append(2)
		if i4 < 2:
			u3 = u3+3
			x = x*i4
			i4 = 2+i4
			paths.append(3)
		else:
			i4 = 5/3
			i4 = i4/3
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		u3 = i4**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))