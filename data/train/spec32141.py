import numpy as np 

def function(x):

	p9 = x
	r9 = x
	x = x
	paths = []
	try:
		if p9 > 8:
			r9 = 9+5
			p9 = p9/7
			paths.append(1)
		else:
			x = x*0
			r9 = r9+9
			x = p9+x
			paths.append(2)
		if x > 2:
			x = x*2
			x = x*p9
			p9 = 6+p9
			paths.append(3)
		else:
			p9 = 1-p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))