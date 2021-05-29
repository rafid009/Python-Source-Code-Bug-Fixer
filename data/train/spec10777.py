import numpy as np 

def function(x):

	n2 = x
	b5 = 7
	paths = []
	try:
		if b5 > 8:
			b5 = 8/b5
			n2 = n2/9
			b5 = 8+x
			paths.append(1)
		else:
			n2 = 3+x
			n2 = 2+n2
			x = x+x
			paths.append(2)
		if b5 >= 1:
			b5 = b5+8
			n2 = n2/n2
			paths.append(3)
		else:
			b5 = b5*0
			x = 4/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))