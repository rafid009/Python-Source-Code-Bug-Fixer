import numpy as np 

def function(x):

	l3 = x
	b6 = x
	paths = []
	try:
		if l3 <= 8:
			b6 = b6/b6
			b6 = b6*x
			paths.append(1)
		else:
			b6 = b6*x
			b6 = b6/2
			x = x/l3
			paths.append(2)
		if b6 >= 7:
			x = 5*0
			x = b6-x
			paths.append(3)
		else:
			x = b6-x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		b6 = l3**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))