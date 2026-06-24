package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MyDequeTest {

    private MyDeque<String> deque;

    @BeforeEach
    void setUp() {
        deque = new MyDeque<>();
    }

    @Test
    void testAddFirst() {
        deque.addFirst("Uno");
        deque.addFirst("Dos");
        assertEquals("Dos", deque.peekFirst());
        assertEquals(2, deque.tamanio());
    }

    @Test
    void testAddLast() {
        deque.addLast("Uno");
        deque.addLast("Dos");
        assertEquals("Dos", deque.peekLast());
        assertEquals(2, deque.tamanio());
    }

    @Test
    void testRemoveFirst() {
        deque.addLast("A");
        deque.addLast("B");
        assertEquals("A", deque.removeFirst());
        assertEquals("B", deque.peekFirst());
        assertEquals(1, deque.tamanio());
    }

    @Test
    void testRemoveLast() {
        deque.addFirst("A");
        deque.addLast("B");
        assertEquals("B", deque.removeLast());
        assertEquals("A", deque.peekLast());
        assertEquals(1, deque.tamanio());
    }

    @Test
    void testIsEmpty() {
        assertTrue(deque.isEmpty());
        deque.addFirst("Algo");
        assertFalse(deque.isEmpty());
    }
}