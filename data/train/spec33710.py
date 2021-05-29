import numpy as np 

def function(x):

	v2 = x
	b1 = x
	paths = []
	try:
		if v2 < 3:
			v2 = v2+b1
			v2 = v2*x
			paths.append(1)
		else:
			x = x*v2
			v2 = 4-v2
			paths.append(2)
		if b1 > 0:
			b1 = b1*x
			paths.append(3)
		else:
			b1 = x+b1
			x = x+x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))