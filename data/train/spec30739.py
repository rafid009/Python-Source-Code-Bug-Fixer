import numpy as np 

def function(x):

	w5 = x
	a1 = 4
	paths = []
	try:
		if a1 > 4:
			x = x/9
			x = x+7
			a1 = a1/2
			paths.append(1)
		else:
			x = x-x
			x = x/1
			paths.append(2)
		if x < 1:
			a1 = a1+1
			x = x*8
			paths.append(3)
		else:
			x = x-0
			w5 = 3+w5
			a1 = w5+a1
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))