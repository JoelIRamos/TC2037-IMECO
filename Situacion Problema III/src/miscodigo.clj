(do
  (println "What's your name?")
  (let [name (read-line)]
    (println (str "Hey, " name))))