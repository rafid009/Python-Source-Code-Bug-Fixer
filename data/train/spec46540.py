import numpy as np 

def function(x):

	n5 = x
	p2 = 4
	paths = []
	try:
		if n5 < 5:
			x = 3+n5
			paths.append(1)
		else:
			x = n5+p2
			n5 = n5*9
			x = p2/5
			paths.append(2)
		if x > 8:
			p2 = x/9
			n5 = n5*x
			p2 = 0+8
			paths.append(3)
		else:
			x = x*0
			x = n5*p2
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))