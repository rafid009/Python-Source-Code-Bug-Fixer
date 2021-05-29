import numpy as np 

def function(x):

	v2 = 5
	t5 = 0
	paths = []
	try:
		if t5 > 5:
			v2 = x*v2
			t5 = t5-v2
			paths.append(1)
		else:
			t5 = t5+v2
			t5 = 6+3
			t5 = t5*t5
			paths.append(2)
		if t5 <= 9:
			x = 5-x
			v2 = t5*2
			v2 = v2*x
			paths.append(3)
		else:
			t5 = 0*t5
			t5 = t5/x
			v2 = 9/v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))