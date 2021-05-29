import numpy as np 

def function(x):

	r7 = 0
	v2 = x
	paths = []
	try:
		if v2 < 7:
			r7 = r7*8
			r7 = r7*x
			paths.append(1)
		else:
			r7 = x*0
			x = 7-7
			r7 = 2+r7
			paths.append(2)
		if x > 5:
			r7 = r7*r7
			r7 = r7-6
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))