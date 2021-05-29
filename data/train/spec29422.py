import numpy as np 

def function(x):

	y5 = 5
	k7 = x
	paths = []
	try:
		if y5 > 8:
			x = x-0
			y5 = 4*y5
			y5 = y5*2
			paths.append(1)
		else:
			x = x+5
			x = x*5
			y5 = y5/7
			paths.append(2)
		if x > 1:
			x = x*8
			x = k7+x
			paths.append(3)
		else:
			y5 = y5*k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))