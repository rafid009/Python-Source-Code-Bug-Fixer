import numpy as np 

def function(x):

	p2 = 7
	r1 = 9
	paths = []
	try:
		if x <= 2:
			p2 = 4*0
			p2 = 5-0
			paths.append(1)
		else:
			x = r1-p2
			paths.append(2)
		if r1 <= 1:
			x = x*8
			p2 = p2-3
			r1 = r1+7
			paths.append(3)
		else:
			x = x/8
			r1 = 5*x
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))