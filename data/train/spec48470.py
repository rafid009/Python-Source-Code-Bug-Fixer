import numpy as np 

def function(x):

	p8 = 2
	e3 = 5
	paths = []
	try:
		if e3 >= 4:
			e3 = p8-7
			p8 = p8/e3
			x = 2*e3
			paths.append(1)
		else:
			p8 = 0*p8
			e3 = 6/e3
			p8 = p8+p8
			paths.append(2)
		if p8 <= 4:
			e3 = 8-9
			p8 = p8-x
			p8 = e3-2
			paths.append(3)
		else:
			e3 = e3*0
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		p8 = e3**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))