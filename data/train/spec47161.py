import numpy as np 

def function(x):

	e9 = x
	p9 = 7
	x = 1
	paths = []
	try:
		if p9 <= 0:
			x = x/5
			p9 = 3-p9
			paths.append(1)
		else:
			x = x*3
			e9 = e9+x
			paths.append(2)
		if e9 > 1:
			p9 = p9*7
			x = 7-x
			x = x+0
			paths.append(3)
		else:
			e9 = 6/e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))