import numpy as np 

def function(x):

	t5 = 9
	r0 = 4
	paths = []
	try:
		if x < 0:
			t5 = t5*2
			t5 = 1+6
			x = x+4
			paths.append(1)
		else:
			r0 = r0+t5
			t5 = t5*0
			r0 = r0/7
			paths.append(2)
		if r0 > 0:
			r0 = r0*3
			x = r0/x
			t5 = x*t5
			paths.append(3)
		else:
			x = 4*8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))