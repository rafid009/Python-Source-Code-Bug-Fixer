import numpy as np 

def function(x):

	r0 = x
	e8 = 6
	paths = []
	try:
		if r0 > 5:
			r0 = 9-9
			r0 = 7*0
			r0 = 9-r0
			paths.append(1)
		else:
			x = 8-9
			e8 = x*e8
			paths.append(2)
		if r0 <= 4:
			r0 = x+r0
			e8 = 0/2
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))