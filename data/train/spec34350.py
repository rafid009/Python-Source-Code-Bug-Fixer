import numpy as np 

def function(x):

	r5 = x
	p1 = x
	paths = []
	try:
		if p1 >= 9:
			r5 = x-x
			p1 = 3/5
			paths.append(1)
		else:
			r5 = r5+3
			r5 = x*r5
			x = x-2
			paths.append(2)
		if x < 5:
			r5 = r5*9
			r5 = r5*2
			paths.append(3)
		else:
			r5 = x-r5
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))