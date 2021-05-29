import numpy as np 

def function(x):

	b2 = 0
	v3 = 7
	paths = []
	try:
		if v3 < 5:
			x = x-x
			x = x*2
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if v3 >= 3:
			b2 = b2*0
			x = x/7
			v3 = 4*v3
			paths.append(3)
		else:
			x = 0/1
			b2 = 0+5
			v3 = 3/v3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))