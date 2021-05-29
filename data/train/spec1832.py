import numpy as np 

def function(x):

	r8 = x
	p2 = 2
	paths = []
	try:
		if p2 <= 6:
			x = p2+6
			r8 = 5-r8
			p2 = p2*p2
			paths.append(1)
		else:
			r8 = r8-r8
			x = x/9
			x = x-8
			paths.append(2)
		if r8 >= 3:
			r8 = r8-5
			x = 6-x
			paths.append(3)
		else:
			r8 = p2-5
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))