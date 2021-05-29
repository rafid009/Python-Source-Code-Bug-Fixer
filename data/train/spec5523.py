import numpy as np 

def function(x):

	r5 = x
	h0 = x
	paths = []
	try:
		if r5 >= 6:
			x = x*1
			paths.append(1)
		else:
			r5 = r5/h0
			h0 = r5-h0
			x = x+r5
			paths.append(2)
		if x <= 7:
			r5 = r5/2
			x = x-x
			paths.append(3)
		else:
			r5 = 5-r5
			h0 = 8*0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		r5 = h0**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))