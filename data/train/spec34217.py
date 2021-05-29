import numpy as np 

def function(x):

	l1 = 4
	i7 = x
	paths = []
	try:
		if x <= 8:
			i7 = l1-7
			x = 6+l1
			i7 = x*i7
			paths.append(1)
		else:
			i7 = i7*5
			x = x-9
			i7 = 9+i7
			paths.append(2)
		if i7 > 8:
			l1 = l1+x
			paths.append(3)
		else:
			l1 = 8*l1
			l1 = l1*6
			l1 = i7*l1
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))