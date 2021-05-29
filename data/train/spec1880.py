import numpy as np 

def function(x):

	t1 = 6
	v3 = 3
	paths = []
	try:
		if v3 < 8:
			v3 = v3*t1
			x = t1-x
			x = x*t1
			paths.append(1)
		else:
			t1 = 4/8
			paths.append(2)
		if x > 3:
			v3 = 1*v3
			v3 = v3/3
			x = x*x
			paths.append(3)
		else:
			t1 = x+0
			v3 = 4-v3
			x = x/t1
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		t1 = v3**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))