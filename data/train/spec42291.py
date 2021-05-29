import numpy as np 

def function(x):

	t2 = 7
	r1 = 5
	paths = []
	try:
		if r1 >= 9:
			t2 = t2-2
			r1 = r1+9
			paths.append(1)
		else:
			t2 = x+0
			x = x-0
			r1 = 9*4
			paths.append(2)
		if t2 <= 7:
			r1 = r1*t2
			paths.append(3)
		else:
			r1 = 0+t2
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		t2 = r1**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))