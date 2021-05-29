import numpy as np 

def function(x):

	n9 = x
	i1 = 2
	paths = []
	try:
		if n9 >= 7:
			x = n9*0
			i1 = x-i1
			n9 = n9+2
			paths.append(1)
		else:
			x = 2+6
			i1 = i1+i1
			paths.append(2)
		if i1 > 6:
			i1 = 5-n9
			x = x*x
			n9 = n9*1
			paths.append(3)
		else:
			x = x+x
			x = x*2
			x = 3/n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))