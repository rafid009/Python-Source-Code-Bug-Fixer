import numpy as np 

def function(x):

	q5 = x
	t8 = x
	paths = []
	try:
		if x > 7:
			t8 = t8-q5
			paths.append(1)
		else:
			x = x*2
			t8 = t8*9
			paths.append(2)
		if q5 >= 8:
			q5 = 4-q5
			paths.append(3)
		else:
			t8 = t8+t8
			q5 = 1+5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		t8 = q5**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))