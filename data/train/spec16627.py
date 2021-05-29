import numpy as np 

def function(x):

	r6 = 4
	t5 = 8
	paths = []
	try:
		if t5 > 2:
			t5 = 0+t5
			t5 = 8-t5
			paths.append(1)
		else:
			x = 4+x
			t5 = t5+3
			x = 1/x
			paths.append(2)
		if t5 <= 7:
			t5 = 3/1
			r6 = t5+x
			r6 = r6*7
			paths.append(3)
		else:
			x = 1+x
			t5 = t5+7
			x = 4*6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		t5 = r6**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))