import numpy as np 

def function(x):

	t5 = x
	m9 = 4
	paths = []
	try:
		if t5 > 5:
			t5 = 3+m9
			x = 6+x
			x = x-m9
			paths.append(1)
		else:
			t5 = 0/t5
			m9 = m9*8
			paths.append(2)
		if x < 9:
			x = 8+x
			x = 8*3
			t5 = 2-4
			paths.append(3)
		else:
			m9 = 8*m9
			m9 = m9/x
			t5 = 8*t5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))