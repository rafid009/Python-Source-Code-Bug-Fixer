import numpy as np 

def function(x):

	k1 = 0
	t5 = 6
	paths = []
	try:
		if x > 4:
			t5 = 5+t5
			t5 = t5/4
			t5 = 0*x
			paths.append(1)
		else:
			k1 = t5*t5
			k1 = k1+4
			t5 = 9*t5
			paths.append(2)
		if x > 1:
			x = t5+8
			x = k1*6
			x = t5+t5
			paths.append(3)
		else:
			t5 = 9+9
			k1 = x+k1
			k1 = 4-t5
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		t5 = k1**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))