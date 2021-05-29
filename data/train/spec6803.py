import numpy as np 

def function(x):

	j8 = x
	b2 = 8
	paths = []
	try:
		if b2 < 0:
			b2 = b2*x
			x = 7+x
			paths.append(1)
		else:
			b2 = b2/4
			b2 = b2/8
			b2 = 2+x
			paths.append(2)
		if b2 < 8:
			b2 = j8*2
			j8 = b2-3
			paths.append(3)
		else:
			b2 = 2+b2
			j8 = b2/2
			j8 = j8-j8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))