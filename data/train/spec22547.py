import numpy as np 

def function(x):

	r2 = 1
	l3 = x
	x = x
	paths = []
	try:
		if l3 > 5:
			r2 = x*l3
			l3 = 5+l3
			l3 = l3*5
			paths.append(1)
		else:
			x = x+2
			l3 = x*l3
			paths.append(2)
		if r2 <= 2:
			r2 = r2-5
			x = x-l3
			x = x-4
			paths.append(3)
		else:
			l3 = x/7
			l3 = l3+r2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		r2 = l3**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))