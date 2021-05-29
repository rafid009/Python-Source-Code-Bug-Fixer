import numpy as np 

def function(x):

	u3 = x
	k7 = 7
	paths = []
	try:
		if k7 > 0:
			u3 = x-1
			k7 = u3+3
			x = x+9
			paths.append(1)
		else:
			k7 = 8*k7
			x = x/2
			paths.append(2)
		if k7 > 7:
			x = x*8
			x = x+x
			k7 = k7-5
			paths.append(3)
		else:
			u3 = 3*x
			k7 = k7/x
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		u3 = k7**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))